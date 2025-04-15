from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import faiss

# Load the data
all_courses_df = pd.read_csv("output_data/output_course_data.csv")
courses_df = all_courses_df.drop_duplicates(subset=["College Course Name"])

data_list = []
#for row in sheet.iter_rows(values_only=True):
#    data_list.append(list(row))

# Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
filename = "output.txt"
f = open(filename, "a")
print("1. Enter a new high school dual enrollment course")
print("2. Search for an existing course")
user_input = input("Select which option you would like to choose (1 or 2)")
while (user_input == "1"):

    input_course_name = input("Enter HS Course Name: ")
    input_course_description = input("Enter a brief course description: ")

    # Process data
    course_embeddings = model.encode(courses_df["HS Course Description"].tolist(), convert_to_numpy=True).astype('float32') # Course Descriptions
    d = course_embeddings.shape[1]


    # Create FAISS similarity search
    index = faiss.IndexFlatL2(d)  # L2 distance index (Euclidean)
    index.add(course_embeddings)  # Add all course vectors to the index

    print(f"FAISS Index contains {index.ntotal} course embeddings.")



    # Convert input course to an embedding
    input_embedding = model.encode([input_course_description], convert_to_numpy=True).astype('float32')

    # Search for the most similar courses
    distances, indices = index.search(input_embedding, k=10) # Find most similar courses


    # Get the top matching courses
    similar_courses = courses_df.iloc[indices[0]].copy()
    similar_courses["Similarity_Score"] = 1 / (1 + distances[0])  # Convert distance to similarity score (higher is better)

    print()
    similar_course_names = similar_courses["College Course Name"]
    similar_course_descriptions = similar_courses["College Course Description"]
    similar_course_colleges = similar_courses["College"]
    similar_course_numbers = similar_courses["College Course"]

    #print("similar names: ", similar_course_names)
    #print("similar desc: ", similar_course_descriptions)
    print("Best Matches: ")
    print("1. ", similar_course_colleges.iloc[0], "offers", similar_course_names.iloc[0], " [", similar_course_numbers.iloc[0], "]")
    print("\t", similar_course_descriptions.iloc[0])
    print()
    print("2. ", similar_course_colleges.iloc[1], "offers", similar_course_names.iloc[1], " [", similar_course_numbers.iloc[1], "]")
    print("\t", similar_course_descriptions.iloc[1])
    print()
    print("3. ", similar_course_colleges.iloc[2], "offers", similar_course_names.iloc[2], " [", similar_course_numbers.iloc[2], "]")
    print("\t", similar_course_descriptions.iloc[2])
    print()
    print("------------------------------------")
    print("These three courses are the best match for your course.")
    decision_input = input("Would you like to see three more possible dual enrollment courses? (Y/N)")
    if (decision_input == 'Y') or (decision_input == 'y'):
        print()
        print("4. ", similar_course_colleges.iloc[3], "offers", similar_course_names.iloc[3], " [", similar_course_numbers.iloc[3], "]")
        print("\t", similar_course_descriptions.iloc[3])
        print()
        print("5. ", similar_course_colleges.iloc[4], "offers", similar_course_names.iloc[4], " [", similar_course_numbers.iloc[4], "]")
        print("\t", similar_course_descriptions.iloc[4])
        print()
        print("6. ", similar_course_colleges.iloc[5], "offers", similar_course_names.iloc[5], " [", similar_course_numbers.iloc[5], "]")
        print("\t", similar_course_descriptions.iloc[5])
        print()
    print("------------------------------")

    yes_no_input = input("Would you like to enter a new course? (Y/N)")
    if not((yes_no_input == 'Y') or (yes_no_input == 'y')):
        user_input = 5

# search by words
while (user_input == "2"):

    search_input = input("What would you like to search for? ")

    column_indices = {}
    column_vectors = {}
    column_texts = {}

    for col in courses_df.columns:
        texts = courses_df[col].astype(str).tolist()
        embeddings = model.encode(texts, convert_to_numpy=True)
        
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)

        column_indices[col] = index
        column_vectors[col] = embeddings
        column_texts[col] = texts
    
    input_embedding = model.encode([search_input], convert_to_numpy=True)[0]

    # Compare input to each column's FAISS index to find best match
    column_similarities = {}

    for col, index in column_indices.items():
        D, I = index.search(np.array([input_embedding]), k=1)  # Top 1 match
        column_similarities[col] = D[0][0]  # Smaller distance = more similar

    # Get the best matching column
    best_column = min(column_similarities, key=column_similarities.get)
    print("Best match column:", best_column)

    # Search the best column for top N similar rows
    index = column_indices[best_column]
    D, I = index.search(np.array([input_embedding]), k=20)

    top_rows = courses_df.iloc[I[0]]
    print(top_rows)

    yes_no_input = input("Would you like to enter a new search term? (Y/N) ")
    if not((yes_no_input == 'Y') or (yes_no_input == 'y')):
        user_input ='5'

print("Closing Dataset...")
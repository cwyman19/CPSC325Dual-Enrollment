// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {GoogleAuthProvider, getAuth} from "firebase/auth";


// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBk4WLQCLNfI4LFU-Cg3_OLlNHRjhr8tLY",
    authDomain: "nwesd-dual-enrollment.firebaseapp.com",
    projectId: "nwesd-dual-enrollment",
    storageBucket: "nwesd-dual-enrollment.firebasestorage.app",
    messagingSenderId: "938728898276",
    appId: "1:938728898276:web:bb29cab15299e7af5eb6f1"
  };

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
export const auth = getAuth(); 
export const googleAuthProvider = new GoogleAuthProvider(); 
export default firebaseApp; 

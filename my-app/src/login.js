import React, { useState, useEffect } from 'react';
import GoogleButton from 'react-google-button'
import { auth, googleAuthProvider} from './firebase.js'
import { signInWithPopup } from 'firebase/auth';
import { useNavigate } from 'react-router-dom';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from "./Home";
import './Login.css';
const Login = () => { 
    const navigate = useNavigate(); 
    const handleSignInWithGoogle = async () => { 
        try { 
            const result = await signInWithPopup(auth, googleAuthProvider);
            localStorage.setItem('Token', result.user.accessToken); 
            localStorage.setItem('user', JSON.stringify(result.user)); 
            navigate("/administrator");
        } catch (error) {
            alert("Unable to Sign in. Try again!"); 
        }
    }
    return (          
      <div className="google-container">
            <GoogleButton onClick={handleSignInWithGoogle} >
            </GoogleButton>
      </div> 
    )
}



export default Login;
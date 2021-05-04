import React, { useState } from "react";
import Signup from "../Components/Signup.js";
import Login from "../Components/Login.js";
import Books from "../Components/books.js";

function Loginpage() {

    const [token, setToken] = useState('');

    const userLogin = (tok) => {
        setToken(tok);
    }
    return (
        <div>
            <Signup userLogin={userLogin} />
            <Login userLogin={userLogin} />
            <Books token={token} />
        </div>

    )
}

export default Loginpage;
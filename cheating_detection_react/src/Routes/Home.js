import React from "react";
import { Link } from "react-router-dom";

class Home extends React.Component {
    render() {
        return (
            <div>
                <span> hello</span>
                <Link to="/ScreenSharing">
                    ScreenSharing
                </Link>
                <div> </div>
                <Link to="/Board">
                    Board
                </Link>
                <div> </div>
                <Link to="/Login">
                    Login
                </Link>

            </div>
        )
    }
}

export default Home;
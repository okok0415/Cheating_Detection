import React from "react";
import {Link} from "react-router-dom";

class Home extends React.Component{
    render() {
        return (
            <div>
                <div>
                Home
                </div>

                <Link to="/ScreenSharing">
                     ScreenSharing
                </Link>
                <div> </div>
                <Link to="/Board">
                    Board
                </Link>

            </div>
        )
    }
}

export default Home;
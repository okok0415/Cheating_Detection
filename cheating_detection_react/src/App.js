import {HashRouter, Route} from "react-router-dom"
import Home from "./Routes/Home.js";
import ScreenSharing from "./Routes/ScreenSharing.js"
import Board from "./Routes/Board.js";
import Detail from "./Routes/Detail.js";

function App() {
  return (
    <HashRouter>
      <Route path="/" exact = {true} component = {Home}/>
      <Route path="/ScreenSharing" exact = {true} component = {ScreenSharing}/>
      <Route path="/Board" exact={true} component={Board}/>
      <Route path="/Board/:id" component={Detail}/>
    </HashRouter>
  );
}

export default App;


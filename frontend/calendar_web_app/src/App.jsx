import React, {useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import { useSelector, useDispatch } from 'react-redux'
import {checkCnx} from './redux/login/loginActions'
import Routing from './routings/routes.jsx'

function App() {
  const connected = useSelector(state => state.login.connected)
  const isLoading = useSelector(state => state.login.loading)
  const dispatch = useDispatch()
  useEffect(() => {
      dispatch(checkCnx());
  }, []);

  return (
    <div className="App">
        <p>connected : {connected.toString()}</p>
        <p>isLoading : {isLoading.toString()}</p>
        <Routing/>
    </div>
  );
}

export default App;

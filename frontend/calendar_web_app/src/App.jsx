import React, {useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import { useSelector, useDispatch } from 'react-redux'
import {checkCnx} from './redux/login/loginActions'
import Routing from './routings/routes.jsx'


function App() {

    const dispatch = useDispatch()
    useEffect(() => {
        dispatch(checkCnx());
    }, []);

    return (
        <div className="App">
            <Routing/>
        </div>
    );
}

export default App;

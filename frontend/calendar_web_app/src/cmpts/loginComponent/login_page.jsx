
import React, {useState, useEffect} from "react";
import axios from 'axios';
import { useHistory } from "react-router-dom";
import {connect} from '../../redux/login/loginActions'
import { useSelector, useDispatch} from 'react-redux'
import wait from '../../statics/wait.gif'
import './styles/login.css';


function Error(props) {
    return (
        <img className="loading" src={wait}/>
    )
}

function LoginPage(props) {
    const [code, setCode] = useState("");
    const [error, setError] = useState("");
    const [pageisLoading, setPageisLoading] = useState(false);
    let history = useHistory();
    const dispatch = useDispatch()
    const connected = useSelector(state => state.login.connected)
    const isLoading = useSelector(state => state.login.loading)

    useEffect(() => {
        if (connected){history.push('/')};
    });

    function login(event){
        event.preventDefault();
        console.log(code);
        setPageisLoading(true)
        axios.post('http://localhost:8000/auth/get_token_from_account/', {code: code})
            .then(function (response) {
                dispatch(connect(response.data.token, code));
                localStorage.setItem('token', response.data.token);
                setPageisLoading(false)
                history.push("/")

            })
            .catch(function (error) {
                setError('erreur');
                setPageisLoading(false)
            })
        setCode("")
    }

    function handleChange(event){
        setCode(event.target.value);
    }

    var x
    if(pageisLoading){
        x = <Error/>
    }

    if(!isLoading){
        return (
            <div className="logwindow">
                <div>
                    <form className="formLog" onSubmit={login}>
                        <label className="labelLog" for="code">Veuillez saisir votre code</label>
                        <input className="txtLog" name="code" type='text' value={code} onChange={handleChange}/>
                        <input className="buttonLog" type='submit' value='Login'/><p>{x}</p>
                        <div className="err">{error}</div>
                    </form>
                </div>
            </div>
        )
    }
    else{
        return(<div>Is Loading</div>)
    }
}

export default LoginPage

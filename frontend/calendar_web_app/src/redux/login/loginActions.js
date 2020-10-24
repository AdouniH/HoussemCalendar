import { CONNECT, DISCONNECT, LOAD } from './loginTypes'
import axios from 'axios';


export const checkCnx = () => {
  return (dispatch) => {
    var tokenKey = localStorage.getItem('token');
    dispatch(load())
    axios
      .post("http://localhost:8000/auth/check_token/", {token: tokenKey})
      .then(response => {
          dispatch(connect(tokenKey, response.data.code));
      })
      .catch(error => {
          dispatch(disconnect());
      })
  }
}

export const connect = (key, code) => {
  return {
    type: CONNECT,
    key: key,
    code: code
  }
}

export const disconnect = () => {
  return {
    type: DISCONNECT,
  }
}

export const load = () => {
  return {
    type: LOAD,
  }
}

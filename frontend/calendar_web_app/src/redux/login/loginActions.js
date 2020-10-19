import { CONNECT, DISCONNECT, LOAD } from './loginTypes'
import axios from 'axios';


export const checkCnx = () => {
  return (dispatch) => {
    var tokenKey = localStorage.getItem('token');
    dispatch(load())
    axios
      .post("http://localhost:8000/auth/check_token/", {token: tokenKey})
      .then(response => {
          dispatch(connect(tokenKey));
      })
      .catch(error => {
          dispatch(disconnect());
      })
  }
}

export const connect = (key) => {
  return {
    type: CONNECT,
    key: key
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

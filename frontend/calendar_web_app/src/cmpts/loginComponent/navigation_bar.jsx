import React from "react";

import { useSelector, useDispatch} from 'react-redux'
import {disconnect} from '../../redux/login/loginActions'
import './styles/navigation_bar.css';

function NavBar() {
  const dispatch = useDispatch();
  const code = useSelector(state => state.login.code);
  const clicked = () => {
      dispatch(disconnect());
      localStorage.removeItem('token')
  }

  return (
    <div className="bar">
        <ul className="deconnexion">
            <li><div className="namec">Connecté : {code}</div></li>
            <li><div className="dcnx" onClick={clicked}>Se deconnecter</div></li>
        </ul>
    </div>
  )
}

export default NavBar

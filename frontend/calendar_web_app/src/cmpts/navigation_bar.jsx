import React from "react";
import './styles/navigation_bar.css';
import { useSelector, useDispatch} from 'react-redux'
import {disconnect} from '../redux/login/loginActions'


function NavBar() {
  const dispatch = useDispatch()

  const clicked = () => {
      dispatch(disconnect());
      localStorage.removeItem('token')
  }

  return (
    <div>
        <ul className="deconnexion">
            <li><div className="dcnx" onClick={clicked}>Se deconnecter</div></li>
        </ul>
    </div>
  )
}

export default NavBar

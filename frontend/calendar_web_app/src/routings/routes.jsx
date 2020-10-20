import React, {useEffect} from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";
import Home from '../cmpts/home.jsx'
import LoginPage from '../cmpts/login_page.jsx'
import {useSelector} from 'react-redux'


function Loading() {
  return (
    <div>
        <h1> Loading </h1>
    </div>
  );
}


const PrivateRoute = ({component: Component, ...rest}) => {
    const connected = useSelector(state => state.login.connected)
    const isLoading = useSelector(state => state.login.loading)
    return (
        <Route {...rest} render={props => (
            isLoading ? <Loading/> :
            isLoading == false && connected == true ? <Component {...props} />
            : <Redirect to="/login" />
        )} />
    );
};


export default function Routing() {
  return (
    <Router>
        <Switch>
            <PrivateRoute exact path="/" component={Home} />
            <Route exact path="/login" component={LoginPage} />
        </Switch>
    </Router>
  );
}

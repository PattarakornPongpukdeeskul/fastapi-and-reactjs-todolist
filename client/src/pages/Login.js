import { useState } from "react"

import { LoginForm, RegisterForm } from "../containers"
import "../styles/login.css"
import "../styles/general.css"
export const Login = () => {
  const [showTabLogin, setShowTabLogin] = useState(true)

  return (
    <div className="login content">
      <div className="login-register-form">
      <div className="tabs">
        <div className={showTabLogin ? 'tab selected' :'tab'} onClick={() => setShowTabLogin(true)}>LOGIN</div>
        <div className={showTabLogin ? 'tab' :'tab selected'} onClick={() => setShowTabLogin(false)}>REGISTER</div>
      </div>
      {showTabLogin ? <LoginForm/> : <RegisterForm/>}
      </div>
    </div>
  )
}

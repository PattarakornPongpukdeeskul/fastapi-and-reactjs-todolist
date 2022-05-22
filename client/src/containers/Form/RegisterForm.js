import { useState } from "react"

import "../../styles/form.css"

export const RegisterForm = () => {
  const [roleRegister, setRoleRegister] = useState("doctor")

  return (
    <div className='form-tab'>
      <form className='form-register'>
        <p className='choose-role'>
          <label>YOU ARE</label>
          <input
            type='radio'
            name='choose_role'
            value='doctor'
            defaultChecked
            onClick={() => setRoleRegister("doctor")}
          />
          <label for='html'>DOCTOR</label>
          <input
            type='radio'
            name='choose_role'
            value='patient'
            onClick={() => setRoleRegister("patient")}
            required
          />
          <label for='css'>PATIENT</label>
        </p>
        {roleRegister === "patient" ? (
          <p>
            <label>YOUR DOCTOR ID'S : </label>
            <input type='text' placeholder='id you get from your doctor'required />
          </p>
        ) : null}
        <p>
          <label>USERNAME : </label>
          <input type='text' placeholder='your name' required />
        </p>
        <p>
          <label>EMAIL ADDRESS : </label>
          <input type='text' placeholder='example@mail.com' required />
        </p>
        <p>
          <label>PASSWORD : </label>
          <input
            type='password'
            name='password'
            placeholder='password'
            required
          />
        </p>
        <p>
          <button type='submit'>Create User</button>
        </p>
      </form>
    </div>
  )
}

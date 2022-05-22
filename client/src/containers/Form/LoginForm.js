import "../../styles/form.css"

export const LoginForm = (name, medicineCount) => {
  return (
    <div className='form-tab'>
      <form className='form-login'>
        <p>
          <label>EMAIL ADDRESS : </label>
          <input type='text' placeholder='example@mail.com' required />
        </p>
        <p>
          <label>PASSWORD : </label>
          <input
            type='password'
            placeholder='password'
            name='password'
            required
          />
        </p>
        <p>
          <button type='submit'>Login</button>
        </p>
      </form>
    </div>
  )
}

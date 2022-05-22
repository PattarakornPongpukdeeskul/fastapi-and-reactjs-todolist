import "../styles/header.css"
import { ReactComponent as IconAccount } from "../assets/svg/icon-account.svg"

export const Header = () => {
  return (
    <header>
      <span className='header-title'>MEDICINE SCHEDULE</span>
      <div class='account'>
        <IconAccount class='icon-account' />
        <ul class='dropdown-content'>
          <li>LOGOUT</li>
          <li>DELETE ACCOUNT</li>
        </ul>
      </div>
    </header>
  )
}

import React from "react"
import { Route, BrowserRouter as Router, Routes } from "react-router-dom"
import { RecoilRoot } from "recoil"
import { Login, Home } from "./pages"
import { Header } from "./components"

export const App = () => {
  return (
    <React.StrictMode>
      <Router>
        <RecoilRoot>
          <Header/>
          <Routes>
            <Route path='/' element={<Login />} />
            <Route path='/home' element={<Home />} />
          </Routes>
        </RecoilRoot>
      </Router>
    </React.StrictMode>
  )
}

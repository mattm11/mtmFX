import React from 'react'
import NavBarLink from './NavBarLink'

function NavigationBar() {
  return (
    <div id="navbar">
        <div className="navtitle">mtmFX.</div>
        <div id="navlinks">
            <NavBarLink path="/" text="Home"/>
            <NavBarLink path="/dashboard" text="Dashboard"/>
        </div>
    </div>
  )
}

export default NavigationBar
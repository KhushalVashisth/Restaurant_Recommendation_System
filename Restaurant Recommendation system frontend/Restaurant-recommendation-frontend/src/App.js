import React from 'react';

import { AboutUs, Footer, Header,  SpecialMenu } from './container';
import { Navbar } from './components';
import './App.css';

const App = () => (
  <div>
    <Navbar />
    <Header />
    <AboutUs />
    <SpecialMenu />
    <Footer />
  </div>
);

export default App;

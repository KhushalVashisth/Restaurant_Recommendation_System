import React from 'react';

import { SubHeading } from '../../components';
import { images } from '../../constants';
import './Header.css';

const Header = () => (
  <div className="app__header app__wrapper section__padding" id="home">
    <div className="app__wrapper_info">
      <SubHeading title="Welcome to Fooder" />
      <h1 className="app__header-h1">The Key To Fine Dining</h1>
      <p className="p__opensans" style={{ margin: '2rem 0' }}>
      Welcome to our premier restaurant recommendation website! We understand that finding the perfect dining experience can be both exciting and challenging. Whether you're a dedicated foodie on the hunt for the latest culinary trends, a couple seeking a romantic dinner spot, a family in search of a kid-friendly eatery, or simply someone who loves good food, our website is here to guide you.{' '}
      </p>
      
    </div>

    <div className="app__wrapper_img">
      <img src={images.welcome} alt="header_img" />
    </div>
  </div>
);

export default Header;

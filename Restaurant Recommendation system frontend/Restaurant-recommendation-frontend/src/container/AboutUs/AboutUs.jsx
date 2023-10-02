import React from 'react';

import { images } from '../../constants';
import './AboutUs.css';

const AboutUs = () => (
  <div
    className="app__aboutus app__bg flex__center section__padding"
    id="about"
  >
    {/* <div className="app__aboutus-overlay flex__center">
      <img src={images.G} alt="G_overlay" />
    </div> */}

    <div className="app__aboutus-content flex__center">
      <div className="app__aboutus-content_about">
        <h1 className="headtext__cormorant">About Us</h1>
        <img src={images.spoon} alt="about_spoon" className="spoon__img" />
        <p className="p__opensans">
        Welcome to our premier restaurant recommendation website! We understand that finding the perfect dining experience can be both exciting and challenging. Whether you're a dedicated foodie on the hunt for the latest culinary trends, a couple seeking a romantic dinner spot, a family in search of a kid-friendly eatery, or simply someone who loves good food, our website is here to guide you.
        </p>
        
      </div>

      <div className="app__aboutus-content_knife flex__center">
        <img src={images.knife} alt="about_knife" />
      </div>

      <div className="app__aboutus-content_history">
        <h1 className="headtext__cormorant">Our History</h1>
        <img src={images.spoon} alt="about_spoon" className="spoon__img" />
        <p className="p__opensans">
        Born from a shared love for food in 2023, we set out to simplify restaurant discovery. Through collaboration with experts and a growing community, we evolved into a platform where culinary enthusiasts share their experiences. Our tech-driven approach introduced interactive maps, dietary filters, and real-time reservations. Today, we're a passionate culinary hub, connecting people with unforgettable dining moments worldwide. Join us to savor the journey!
        </p>
        
      </div>
    </div>
  </div>
);

export default AboutUs;

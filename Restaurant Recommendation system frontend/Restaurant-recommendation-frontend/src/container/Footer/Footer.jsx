import React from 'react';
import { FiFacebook, FiTwitter, FiInstagram } from 'react-icons/fi';

import { FooterOverlay, Newsletter } from '../../components';
import { images } from '../../constants';
import './Footer.css';

const Footer = () => (
  <div className="app__footer section__padding" id="login">
    <FooterOverlay />
    <Newsletter />

    <div className="app__footer-links">
      <div className="app__footer-links_contact">
        <h1 className="app__footer-headtext">Contact Us</h1>
        {/* <p className="p__opensans">Address bhi nahi bataunga</p> */}
        <p className="p__opensans">+91 9748784377</p>
        <p className="p__opensans">+91 7836743678</p>
      </div>

      <div className="app__footer-links_logo">
        <img src={images.logoo} alt="footer_logo" />
        <p className="p__opensans">
          &quot;One Stop Solution for all the Foodies&quot;
        </p>
        <img
          src={images.spoon}
          className="spoon__img"
          style={{ marginTop: 15 }}
        />
        <div className="app__footer-links_icons">
          <FiFacebook />
          <FiTwitter />
          <FiInstagram />
        </div>
      </div>

      <div className="app__footer-links_work">
        <h1 className="app__footer-headtext">Mail us at</h1>
        <p className="p__opensans">helpline@fooder.com</p>
        <p className="p__opensans">foodergo@gmail.com</p>
        {/* <p className="p__opensans"></p>
        <p className="p__opensans"></p> */}
      </div>
    </div>

    <div className="footer__copyright">
      <p className="p__opensans">2023 Fooder. All Rights reserved.</p>
    </div>
  </div>
);

export default Footer;

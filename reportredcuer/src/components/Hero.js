import React from 'react';
import './css/hero.css';
import Typewriter from 'typewriter-effect';
import { Link } from 'react-scroll';

export default function Hero() {
    return (
        <div className="hero-wrapper">
            <div className="hero-content">
                <div className='text'>
                    <h1>
                        <Typewriter
                            options={{
                                strings: ['Report Reducer'],
                                autoStart: true,
                                loop: true,
                            }}
                        />
                    </h1>
                    <p>
                        Save time, invest, grow with Report Reducer
                    </p>
                    <Link to="target-section" smooth={true} duration={10}>
                        <button className='button-down'>Get Started Below</button>
                    </Link>
                </div>
            </div>
        </div>
    );
}

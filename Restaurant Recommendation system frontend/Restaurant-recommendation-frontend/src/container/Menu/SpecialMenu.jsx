import React, {useState} from 'react';

import { SubHeading, MenuItem } from '../../components';
import { data, images } from '../../constants';
import './SpecialMenu.css';


const SpecialMenu = () => {


  const [costRange, setCostRange] = useState([0, 9999]);
  const [selectedOption1, setSelectedOption1] = useState(0);
  const [selectedOption2, setSelectedOption2] = useState('');
  const [selectedOption3, setSelectedOption3] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const handleMinCostChange = (event) => {
    const minValue = parseInt(event.target.value);
    setCostRange([minValue, costRange[1]]);
  };

  const handleMaxCostChange = (event) => {
    const maxValue = parseInt(event.target.value);
    setCostRange([costRange[0], maxValue]);
  };
  const handleSelect1Change = (event) => {
    setSelectedOption1(event.target.value);
  };

  const handleSelect2Change = (event) => {
    setSelectedOption2(event.target.value);
  };

  const handleSelect3Change = (event) => {
    setSelectedOption3(event.target.value);
  };




  const onSubmit = async() =>{
    let url = '';
    // let respone = '';
    console.log("pressed");
    // console.log(selectedOption1)
    console.log(selectedOption2);
    // switch(city){
    //   case 'delhi':
    //     switch(selectedOption){
    //       case 'input1':
    //         url='http://127.0.0.1:5000/get_recommendationsCostDelhi'
    //         break;
    //       case 'input2':
    //         url = 'http://127.0.0.1:5000/get_recommendationsRatingDelhi'
    //         break;
    //       case 'input3':
    //         url = 'http://127.0.0.1:5000/get_recommendationsLikeDelhi'
    //         break;
    //       case 'input4':
    //         url = 'http://127.0.0.1:5000/get_recommendationsCuisineDelhi'
    //         break;
    //       default:
    //         break
    //     }
    //   case 'bangalore':
    //     switch(selectedOption){
    //       case 'input1':
    //         url='http://127.0.0.1:5000/get_recommendationsCost'
    //         break;
    //       case 'input2':
    //         url = 'http://127.0.0.1:5000/get_recommendationsRating'
    //         break;
    //       case 'input3':
    //         url = 'http://127.0.0.1:5000/get_recommendationsLike'
    //         break;
    //       case 'input4':
    //         url = 'http://127.0.0.1:5000/get_recommendationsCuisine'
    //         break;
    //       default:
    //         break;
    //     }
    //   default:
    //     break;
    // }


    // const response = await fetch('http://127.0.0.1:5000/get_recommendationsRating', {
      if(city === 'delhi' && selectedOption === 'input2'){
          url='http://127.0.0.1:5000/get_recommendationsRatingDelhi'
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
          });
          const data = await response.json();
          const recommendationsArray = JSON.parse(data.recommendations);
          setRecommendations(recommendationsArray);
      }
      else if(city === 'delhi' && selectedOption === 'input1'){
        url='http://127.0.0.1:5000/get_recommendationsCostDelhi'
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data1: parseInt(costRange[0]), user_data2: parseInt(costRange[1]) }),
          });
          const data = await response.json();
          const recommendationsArray = JSON.parse(data.recommendations);
          setRecommendations(recommendationsArray);
      }
      else if(city === 'delhi' && selectedOption === 'input3'){
        url='http://127.0.0.1:5000/get_recommendationsLikeDelhi'
        console.log(url);
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data: selectedOption2 }),
          });
          const data = await response.json();
          console.log(data);
          const recommendationsArray = JSON.parse(data.recommendations);
          setRecommendations(recommendationsArray);
      }
      else if(city === 'delhi' && selectedOption === 'input4'){
        url='http://127.0.0.1:5000/get_recommendationsCuisineDelhi'
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data:selectedOption3 }),
          });
          const data = await response.json();
          console.log(data.recommendations)
          const recommendationsArray = JSON.parse(data.recommendations);
          setRecommendations(recommendationsArray);
      }

      else if(city === 'bangalore' && selectedOption === 'input1'){
        url='http://127.0.0.1:5000/get_recommendationsCost'
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data1: parseInt(costRange[0]), user_data2: parseInt(costRange[1]) }),
          });
          const data = await response.json();
          const recommendationsArray = JSON.parse(data.recommendations);
          setRecommendations(recommendationsArray);
      }
      else if(city === 'bangalore' && selectedOption === 'input2'){
        url='http://127.0.0.1:5000/get_recommendationsRating'
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data:parseInt(selectedOption1) }),
          });
          const data = await response.json();
          const recommendationsArray = JSON.parse(data.recommendations);
          setRecommendations(recommendationsArray);
      }
      
      else if(city === 'bangalore' && selectedOption === 'input3'){
        url='http://127.0.0.1:5000/get_recommendationsLike'
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data:selectedOption2 }),
          });
          const data = await response.json();
          const recommendationsArray = JSON.parse(data.recommendations);
          setRecommendations(recommendationsArray);
      }

      else if(city === 'bangalore' && selectedOption === 'input4'){
        url='http://127.0.0.1:5000/get_recommendationsCuisine'
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            // body: JSON.stringify({ user_data: parseInt(selectedOption1) }),
            body: JSON.stringify({ user_data:selectedOption3 }),
          });
          const data = await response.json();
          const recommendationsArray = JSON.parse(data.recommendations);

          setRecommendations(recommendationsArray);
      }

      




      console.log(url);
      console.log(city)
    // const data = await response.json();
    // const recommendationsArray = JSON.parse(data.recommendations);
    // setRecommendations(recommendationsArray);
    console.log(data);
    console.log(recommendations);
  }



  const [selectedOption, setSelectedOption] = useState(null);
  const [city,setCity] = useState(null);

  const handleOptionChangeCity = (option) => {
    setCity(option);
  };
  // const [type, setType] = useState(null);
  const handleOptionChange = (option) => {
    setSelectedOption(option);
  };






  return(

  <div className="app__specialMenu flex__center section__padding" id="menu">
      {/* <form onSubmit={onSubmit}> */}
      {/* <form> */}
    <div className="app__specialMenu-title">
      <SubHeading title="Select your filters" />
      <h1 className="headtext__cormorant">Recommendation</h1>

      


<div className='p__opensans'>

<form style={{display:'inline-block'}}>
  <div className='radiocity radiogroup'>
        <label>
          <input className='radcity'
            type="radio"
            name="option"
            value="option1"
            onChange={() => handleOptionChangeCity('delhi')}
          />
          DELHI
        </label>
        <br />
        <label>
          <input className='radcity'
            type="radio"
            name="option"
            value="option2"
            onChange={() => handleOptionChangeCity('bangalore')}
          />
          BANGALORE
        </label>
        </div>
      </form>
    </div>






{/* FOR FUNCTION TYPES */}
<div className='p__opensans'>
<form style={{display:'inline-block'}}>
  <div className='radiogroup'>
        <label>
          <input
            type="radio"
            name="option"
            value="option1"
            onChange={() => handleOptionChange('input1')}
          />
          Cost
        </label>
        <br />
        <label>
          <input
            type="radio"
            name="option"
            value="option2"
            onChange={() => handleOptionChange('input2')}
          />
          Rating
        </label>
        <br />
        <label>
          <input
            type="radio"
            name="option"
            value="option4"
            onChange={() => handleOptionChange('input4')}
          />
          Cuisines
        </label>
        <label>
          <input
            type="radio"
            name="option"
            value="option3"
            onChange={() => handleOptionChange('input3')}
          />
          Similar Restaurants
        </label>
        <br />
        </div>
      </form>
      </div>

      <div className="p__opensans">
      {selectedOption === 'input1' && (
      <div className='inputss'>
        <label htmlFor="minCost">Min Cost:</label>
        <input
          type="range"
          id="minCost"
          min={1}
          max={9998}
          value={costRange[0]}
          onChange={handleMinCostChange}
        />
        <div>Min: {costRange[0]}</div>
      </div>
      )}

      {selectedOption === 'input1' && (
      <div>
        <label htmlFor="maxCost">Max Cost:</label>
        <input
          type="range"
          id="maxCost"
          min={1}
          max={8500}
          value={costRange[1]}
          onChange={handleMaxCostChange}
        />
        <div>Max: {costRange[1]}</div>
      </div>
      )}

      {selectedOption === 'input2' && (
      <div className='inputss'>
        <label htmlFor="select1">Minimum Rating:</label>
        <select id="select1" value={selectedOption1} onChange={handleSelect1Change}>
          <option value="">Select an option</option>
          <option value={5}>5</option>
          <option value={4}>4</option>
          <option value={3}>3</option>
          <option value={2}>2</option>

        </select>
      </div>
      )}

      {selectedOption === 'input3' && (
      <div className='inputss'>
        <label htmlFor="select2">Enter Restaurant Name:</label>
        {/* <select id="select2" value={selectedOption2} onChange={handleSelect2Change}>
          <option value="">Select an option</option>
          <option value="option4">Option 4</option>
          <option value="option5">Option 5</option>
          <option value="option6">Option 6</option>
        </select> */}
        <input type="text" name="username" id="username" placeholder="Enter here" value={selectedOption2} onChange={handleSelect2Change}/>
      </div>
      )}
      {selectedOption === 'input4' && (
      <div className='inputss'>
        <label htmlFor="select3">Enter Cuisine:</label>
        {/* <select id="select3" value={selectedOption3} onChange={handleSelect3Change}>
          <option value="">Select an option</option>
          <option value="option7">Option 7</option>
          <option value="option8">Option 8</option>
          <option value="option9">Option 9</option>
        </select> */}
        <input type="text" name="usernamee" id="usernamee" placeholder="Enter here" value={selectedOption3} onChange={handleSelect3Change}/>
      </div>
      )}
    </div>


    </div>

    

  


    

    <div style={{ marginTop: 15 }}>
      <button className="custom__button" onClick={onSubmit}>
        Submit
      </button>
    </div>
    {/* </form> */}


    {/* <div className="recommendations p__opensans">
        <h2>Recommendations:</h2>
        <ul>
          {recommendations.map((recommendation, index) => (
            <li key={index}>{recommendation}</li>
          ))}
        </ul>
      </div> */}


      {/* <div className="recommendations p__opensans">
        <h2>Recommendations:</h2>
        <ul>
          {recommendations.map((recommendation, index) => (
            <li key={index}>{recommendation}</li>
          ))}
        </ul>
      </div> */}

      <div className="recommendations p__opensans">
        <h2>Recommendations:</h2>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Cuisines</th>
              <th>Mean Rating</th>
              <th>Cost</th>
            </tr>
          </thead>
          <tbody>
            {recommendations.map((recommendation, index) => (
              <tr key={index}>
                <td>{recommendation.name}</td>
                <td>{recommendation.cuisines}</td>
                <td>{recommendation['Mean Rating']}</td>
                <td>{recommendation.cost}</td>
              </tr>
            ))}
          </tbody>
        </table>


      </div>




  </div>
);
  };

export default SpecialMenu;

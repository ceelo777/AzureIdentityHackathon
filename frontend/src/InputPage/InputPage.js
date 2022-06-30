import React from 'react';
import './InputPage.css';

class InputPage extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: 'Please input an email!',
        regEx: new RegExp("^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$")
      }
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {            
      this.setState({value: event.target.value});      
    }
  
    handleSubmit(event) {
      const requestOptions = {
        mode: 'cors',
        method: 'POST',        
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify( { text: this.state.value } )
      };
      fetch('http://localhost:5000/submitText', requestOptions)
        .then(response => {return response.json();})
        .then(responseData => console.log("Response Data: ", responseData));
      event.preventDefault();
    }

    render() {
      return (
        <div className="component-div">                    
          <div className="form-div">              
              <form onSubmit={this.handleSubmit}>                                
                  <textarea value={this.state.value} onChange={this.handleChange}></textarea>
                  <div className="submit-button">
                      <input type="submit" value="Submit" />
                  </div>
              </form>
          </div>
          <div className="output-div">
          </div>
        </div>
      );
    }
  }

  export default InputPage;
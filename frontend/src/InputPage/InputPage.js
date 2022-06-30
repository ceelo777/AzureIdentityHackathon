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
      this.state.value.split(" ").forEach(word => {
        if (this.state.regEx.test(word)) {
            console.log("Password found: ", word);
        }
      });
      this.setState({value: "<div>hello</div>"});      
    }
  
    handleSubmit(event) {
      const requestOptions = {
        mode: 'cors',
        method: 'POST',        
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify( { text: this.state.value } )
      };
      fetch('http://localhost:5000/submitText', requestOptions)
        .then(response => console.log("Response: ", response))
      event.preventDefault();
    }

    render() {
      return (
        <div className="form-div">
            <div className="title">Try sending an email...</div>
            <form onSubmit={this.handleSubmit}>                
                <label>                    
                    <textarea value={this.state.value} onChange={this.handleChange} />
                </label>
                <div className="submit-button">
                    <input type="submit" value="Submit" />
                </div>
            </form>
        </div>
      );
    }
  }

  export default InputPage;
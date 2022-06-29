import React from 'react';
import './InputPage.css';

class InputPage extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: 'Please input an email!'
      };
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({value: event.target.value});
    }
  
    handleSubmit(event) {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify( { text: this.state.value } )
      };
      fetch('http://localhost:5000/submitText', requestOptions)
        .then(response => response.json())
        .then(data => console.log(data));
      event.preventDefault();
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            Email:
            <textarea value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
      );
    }
  }

  export default InputPage;
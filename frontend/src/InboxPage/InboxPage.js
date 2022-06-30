import React from 'react';
import status_data from '../json_data_status.json';
import data from './json_data.json';

import './InboxPage.css';

class InboxPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      entries: [],
      listItems: null,
      status: status_data
    }    
  }

  handleSubmit(event) {
    const requestOptions = {
      mode: 'cors',
      method: 'GET',        
      headers: { 'Content-Type': 'application/json' },
    };
    fetch('http://localhost:5000/parseInbox', requestOptions)
      .then(data => { 
        console.log(data);
        // this.setState({status: true}) 
      });    
  }

  componentDidMount() {
    const that = this;
    const requestOptions = {
      mode: 'cors',
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    };
    fetch('http://localhost:5000/showInbox', requestOptions)
      .then(response => {
        console.log(response);
      })
  }

  render() {
    console.log("Data: ", data);
    let listItems = [];
    let idx = 0;    
    // Email Address: {entry.from.emailAddress.address} - Data: {entry.subject}        
    //let listItems = ; 
    // let listItems = [<li>awef</li>, <li>goodbye</li>];
    console.log("Status: ", this.state.status);
    let keys = [];
    for (const [key, value] of Object.entries(this.state.status)) {
      keys.push(key);
    }
    data.value.forEach(entry => {
      listItems.push(        
          <tr>
            <td>{entry.from.emailAddress.name}</td>              
            <td>{entry.from.emailAddress.address}</td>                      
            <td>{entry.subject}</td>                        
            <td>{this.state.status[keys[idx]]}</td>
          </tr>  
      )        
      idx++;
    });
    return (
      <div className="inbox-page-div">
        <div className="table-form">
          <table>
            <tbody>
            <tr className="subject-header">
              <td>Names</td>
              <td>Email Addresses</td>
              <td>Emails</td>                            
            </tr>          
            {listItems}
            </tbody>
          </table>
          
        </div>
        <form onSubmit={this.handleSubmit}>
          <div className="submit-div-button">
            <input type="submit" value="Submit" />
          </div>
        </form>
      </div>
    );
  }
}

export default InboxPage;
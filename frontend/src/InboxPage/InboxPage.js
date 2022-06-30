import React from 'react';
import data from './json_data.json';
import './InboxPage.css';

class InboxPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      entries: [],
      listItems: null
    }
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
    data.value.forEach(entry => {
      listItems.push(        
          <tr>
            <td>{entry.from.emailAddress.name}</td>              
            <td>{entry.from.emailAddress.address}</td>                      
            <td>{entry.subject}</td>
          </tr>  
      )        
    });
    // Email Address: {entry.from.emailAddress.address} - Data: {entry.subject}        
    //let listItems = ; 
    // let listItems = [<li>awef</li>, <li>goodbye</li>];
    return (
      <div className="table-form">
        <table>
          <tr className="subject-header">
            <td>Names</td>
            <td>Email Addresses</td>
            <td>Emails</td>
          </tr>          
          {listItems}
        </table>      
      </div>
    );
  }
}

export default InboxPage;
import React from 'react';
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
        const requestOptions = {
            mode: 'cors',
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
          };      
        fetch('http://localhost:5000/showInbox', requestOptions)
        .then(response => {                        
            return response.json();                    
        })
        .then(responseData => {
            let entries = [];
            responseData.value.forEach(val => {
                entries.push(val);                    
            })
            this.setState({entries: entries});            
        })         
    }

    render() {        
        let listItems = this.state.entries.map((entry) => {
            <li>
                Email Address: {entry.from.emailAddress.address} - Data: {entry.subject}
            </li>
        });
        console.log("List Items: " + listItems);
      return (        
        <div className="form-div">
            <ul>
                {listItems ? listItems : <div></div>}
            </ul>                        
        </div>
      );
    }
  }

  export default InboxPage;
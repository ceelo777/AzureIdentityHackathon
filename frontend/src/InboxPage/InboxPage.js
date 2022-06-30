import React from 'react';
import './InboxPage.css';

class InboxPage extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        entries: []
      }
      
      const requestOptions = {
        mode: 'cors',
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      };

      fetch('http://localhost:5000/parseInbox', requestOptions)
        .then(response => {
            console.log("Inbox: ", response);
        });
    }

    render() {
      return (
        <div className="form-div">

        </div>
      );
    }
  }

  export default InboxPage;
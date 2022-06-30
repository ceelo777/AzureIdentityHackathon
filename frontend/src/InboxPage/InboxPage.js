import React from 'react';
import './InboxPage.css';

class InboxPage extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: 'Please input an email!',
        regEx: new RegExp("^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$")
      }
    }

    render() {
      return (
        <div className="form-div">
        </div>
      );
    }
  }

  export default InboxPage;
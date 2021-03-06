import React from 'react';
import moment from 'moment';

class Card extends React.Component {
  render() {
    return (<div className="row">
      <div className="col">
        <div className="card">
          <div className="card-image">
            <img src={this.props.imageUrl}/>
            {/*<span class="card-title">Card Title</span>*/}
          </div>
          <div className="card-content">
            <span className="card-title">{moment(this.props.date).format('DDD MMM YYYY')}</span>
            <span className="card-title">{this.props.name}</span>
            <p>{this.props.description}</p>
          </div>
          <div className="card-action">
            {/*<a href="#">This is a link</a>*/}
            {/*<a href="#">This is a link</a>*/}
          </div>
        </div>
      </div>
    </div>);
  }
}

export default class Dash extends React.Component {
  renderCards() {
    let trips = this.props.tripStore.trips;
    let cards = [
      {
        name: 'Hackathon',
        start_date: '2/3/2018',
        imageUrl: 'http://www.developerweek.com/wp-content/uploads/2015/11/hackaton-banner-badge.png'
      },
      {
        name: 'Football',
        start_date: '2/3/2018',
        imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/81DBe4NVTiL._SL1500_.jpg'
      }
    ];
    cards = cards.concat(trips);
    return cards.map(x => {
      return <Card
        name={x.name}
        date={x.start_date}
        imageUrl={x.imageUrl || 'http://www.developerweek.com/wp-content/uploads/2015/11/hackaton-banner-badge.png'}
      />
    });
  }
  render() {
    console.log(this.state);
    return (<div className={"dash-container"}>
      <div className={"row"}>
        <div className={"create-button col"}>
          <a className="waves-effect waves-light btn">Create New Trip</a>
        </div>
      </div>
      {/*<div className={"create-button"}>Create New Trip</div>*/}
      {this.renderCards()}
    </div>);
  }
}

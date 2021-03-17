import React from 'react';
import './App.css';

class App extends React.Component{
  constructor(props){
    super(props);
      this.state = {
        roomList:[],
        activeItem:{
          id:null,
          title:'',
          completed:false,
        },
        editing:false,
      }
      this.fetchTasks = this.fetchTasks.bind(this)
  };

  componentWillMount(){
    this.fetchTasks()
  }

  fetchTasks(){
    fetch('http://127.0.0.1:8000/api/')
    .then(reponse => reponse.json())
    .then(data=>
      this.setState({
        roomList:data
      })
      )
  }
  handleChange(e){

  }

  render(){
    var rooms = this.state.roomList
    console.log('rooms', rooms)
    return(
      <div className="container">
        <div id="task-container">
          <div  id="form-wrapper">
            <form id="form">
              <div className="flex-wrapper">
                <div style={{flex: 6}}>
                    <input className="form-control" id="title" type="text" name="title" placeholder="Add task.." />
                </div>
                <div style={{flex: 1}}>
                    <input id="submit" className="btn btn-warning" type="submit" name="Add" />
                </div>
              </div>
            </form>             
          </div>
        </div>  
        <div id="list-wrapper">
          {rooms.map(function(room, index){
            return(
              <div key={index} className="task-wrapper flex-wrapper">
                <div style={{flex:7}}>
                  <span>{room.room_name}: </span>
                  <span>{room.room_description} </span>
                  <span><img src={room.room_image}/>{room.room_image}</span><br></br>
                  <span>{room.room_type}</span><br></br>
                  <span>Customer Rating: {room.room_ratings}</span><br></br>
                  <span>Price per Night: £{room.room_price_per_night}</span>
                </div>
                <div style={{flex:1}}>
                  <button className="btn btn-sm btn-outline-info m-1">Edit</button>
                </div>
                <div style={{flex:1}}>
                <button className="btn btn-sm btn-outline-dark m-1">Delete</button>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    )
  }
}



export default App;

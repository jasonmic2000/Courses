import './App.css';
import React, { useState } from 'react'
import Title from './components/Title'
import Modal from './components/Modal'

function App() {
  const [showEvents, setShowEvents] = useState(true)
  const [events, setEvents] = useState([
    {title: "mario's birthday bash", id: 1},
    {title: "bowser's live stream", id: 2},
    {title: "race on moo moo farm", id: 3}
  ])

  console.log(showEvents)

  const handleClick = (id) => {
    setEvents((prevEvents) => {
      return prevEvents.filter((event) => {
        return id !== event.id
      })
    })
    console.log(id)
  }

  const subtitle = "All the latest events in Marioland"

  return (
    <div className="App">
      <Modal />
      <Title title="Events in Your Area" subtitle={subtitle} />

      {showEvents && (
        <div>
          <button onClick={() => setShowEvents(false)}>hide events</button>
        </div>
      )}

      {!showEvents && (
        <div>
          <button onClick={() => setShowEvents(true)}>show events</button>
        </div>
      )}
      {showEvents && events.map((event, index) => (
        <React.Fragment key={event.id}>
          <h2>{index} - {event.title}</h2>
          <button onClick={() => handleClick(event.id)}>Delete event</button>
        </React.Fragment>
      ))}

      {/* <Modal>
        <h2>10% off Coupon Code!!</h2>
        <p>Use the code POTATOES at checkout.</p>
      </Modal> */}

      <Modal>
        <h2>Terms and Conditions</h2>
        <p>Laboris consectetur eiusmod occaecat tempor do in aute esse eu quis velit. Sit ea exercitation dolor do qui cillum non. Do ex elit laborum quis duis veniam et elit ad est anim. Cupidatat laboris adipisicing non non commodo proident eiusmod ullamco nostrud consequat. Dolor laborum reprehenderit anim ea anim commodo proident veniam irure elit ullamco excepteur nisi. Do aliqua tempor amet ipsum non et consequat culpa do. Incididunt do magna aliqua aliqua adipisicing proident aute sunt non ut anim nostrud in.</p>
        <a href="#">find out more...</a>

      </Modal>
    </div>
  );
}

export default App;

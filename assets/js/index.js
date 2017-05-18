var React = require('react')
var ReactDOM = require('react-dom')

var PlayerList = React.createClass({
    loadPlayersFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadPlayersFromServer();
        setInterval(this.loadPlayersFromServer,
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var playerNodes = this.state.data.map(function(player){
                return <li> {player.name} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {playerNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<PlayerList url='/store/player/' pollInterval={1000} />,
    document.getElementById('container'))
var chat = {
    ws_url: 'ws://' + window.location.host + window.location.pathname + 'chat/',

    initialize: function() {
        chat.socket = new WebSocket(chat.ws_url);

        chat.socket.onopen = function(e) {
            chat.update_status('Connected to chat');
        };

        chat.socket.onerror = function(e) {
            chat.update_status('Chat error');
        };

        chat.socket.onclose = function(e) {
            chat.update_status('Disconnected from chat');
        };

        chat.socket.onmessage = function(e) {
            var payload = JSON.parse(e.data);
            var user = payload['message']['user'];
            var msg = payload['message']['message'];
            chat.append_message(user, msg);
        };
    },

    update_status: function(message) {
        $('#status').html(message);
    },

    append_message: function(user, message) {
        text = user + ": \n" + message + '\n\n';
        $('#chat').append(text);
    },

    send_message: function(message) {
        data = {'message': message};
        chat.socket.send(JSON.stringify(data));
    }
}
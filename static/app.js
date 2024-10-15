new Vue({
    el: '#app',
    data: {
        rooms: [],
        newRoom: { name: '' },
        newPerson: { name: '' },
        selectedRoomId: null
    },
    methods: {
        fetchRooms() {
            axios.get('/api/rooms')
                .then(response => {
                    this.rooms = response.data;
                })
                .catch(error => console.error('Error fetching rooms:', error));
        },
        addRoom() {
            axios.post('/api/rooms', { id: Date.now(), name: this.newRoom.name })
                .then(response => {
                    this.rooms.push(response.data);
                    this.newRoom.name = '';
                })
                .catch(error => console.error('Error adding room:', error));
        },
        addPerson() {
            if (!this.selectedRoomId) return;
            axios.post(`/api/rooms/${this.selectedRoomId}/occupants`, { id: Date.now(), name: this.newPerson.name })
                .then(response => {
                    const updatedRoom = response.data;
                    const index = this.rooms.findIndex(room => room.id === updatedRoom.id);
                    if (index !== -1) {
                        this.rooms.splice(index, 1, updatedRoom);
                    }
                    this.newPerson.name = '';
                })
                .catch(error => console.error('Error adding person:', error));
        }
    },
    mounted() {
        this.fetchRooms();
    }
});
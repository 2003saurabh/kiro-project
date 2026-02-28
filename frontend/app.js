const API_URL = 'http://localhost:5000/api';

async function fetchItems() {
    try {
        const response = await fetch(`${API_URL}/items`);
        const items = await response.json();
        displayItems(items);
    } catch (error) {
        console.error('Error fetching items:', error);
    }
}

function displayItems(items) {
    const itemList = document.getElementById('itemList');
    itemList.innerHTML = '';
    items.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${item.name}</span>
            <button class="delete-btn" onclick="deleteItem(${item.id})">Delete</button>
        `;
        itemList.appendChild(li);
    });
}

async function addItem() {
    const itemName = document.getElementById('itemName').value;
    if (!itemName) {
        alert('Please enter an item name');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/items`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: itemName })
        });
        
        if (response.ok) {
            document.getElementById('itemName').value = '';
            fetchItems();
        }
    } catch (error) {
        console.error('Error adding item:', error);
    }
}

async function deleteItem(id) {
    try {
        const response = await fetch(`${API_URL}/items/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            fetchItems();
        }
    } catch (error) {
        console.error('Error deleting item:', error);
    }
}

// Load items on page load
fetchItems();

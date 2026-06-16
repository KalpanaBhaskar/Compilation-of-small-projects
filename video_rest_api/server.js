const express = require('express');
const app = express();
const PORT = 3000;

// Middleware to allow Express to read JSON data from Postman requests
app.use(express.json());

// Our "Database" (a simple in-memory array)
let games = [
    { id: 101, title: "Super Mario Bros", platform: "NES", price: 29.99, inStock: true },
    { id: 102, title: "Sonic the Hedgehog", platform: "Sega Genesis", price: 24.99, inStock: true }
];

// --- 1. GET ALL GAMES ---
app.get('/v1/games', (req, res) => {
    res.status(200).json(games);
});

// --- 2. GET A SINGLE GAME BY ID ---
app.get('/v1/games/:id', (req, res) => {
    const gameId = parseInt(req.params.id);
    const game = games.find(g => g.id === gameId);

    if (!game) {
        return res.status(404).json({ message: "Game not found" });
    }
    res.status(200).json(game);
});

// --- 3. POST (CREATE A NEW GAME) ---
app.post('/v1/games', (req, res) => {
    // Generate a new unique ID based on the last item's ID
    const newId = games.length > 0 ? games[games.length - 1].id + 1 : 101;
    
    const newGame = {
        id: newId,
        title: req.body.title,
        platform: req.body.platform,
        price: req.body.price,
        inStock: req.body.inStock
    };

    games.push(newGame);
    res.status(201).json(newGame);
});

// --- 4. PUT (REPLACE AN ENTIRE GAME) ---
app.put('/v1/games/:id', (req, res) => {
    const gameId = parseInt(req.params.id);
    const gameIndex = games.findIndex(g => g.id === gameId);

    if (gameIndex === -1) {
        return res.status(404).json({ message: "Game not found to replace" });
    }

    // Completely replace the object at that index
    games[gameIndex] = {
        id: gameId, // keep the same ID
        title: req.body.title,
        platform: req.body.platform,
        price: req.body.price,
        inStock: req.body.inStock
    };

    res.status(200).json(games[gameIndex]);
});

// --- 5. PATCH (PARTIALLY UPDATE A GAME) ---
app.patch('/v1/games/:id', (req, res) => {
    const gameId = parseInt(req.params.id);
    const game = games.find(g => g.id === gameId);

    if (!game) {
        return res.status(404).json({ message: "Game not found to update" });
    }

    // Only update fields if they were provided in the request body
    if (req.body.title !== undefined) game.title = req.body.title;
    if (req.body.platform !== undefined) game.platform = req.body.platform;
    if (req.body.price !== undefined) game.price = req.body.price;
    if (req.body.inStock !== undefined) game.inStock = req.body.inStock;

    res.status(200).json(game);
});

// --- 6. DELETE A GAME ---
app.delete('/v1/games/:id', (req, res) => {
    const gameId = parseInt(req.params.id);
    const gameIndex = games.findIndex(g => g.id === gameId);

    if (gameIndex === -1) {
        return res.status(404).json({ message: "Game not found to delete" });
    }

    // Remove the game from the array
    games.splice(gameIndex, 1);
    res.status(200).json({ message: `Game with ID ${gameId} has been deleted` });
});

// Start the server
app.listen(PORT, () => {
    console.log(`🚀 Server is running live at http://localhost:${PORT}`);
});
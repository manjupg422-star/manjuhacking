// weather_dashboard.js

const apiKey = 'YOUR_API_KEY'; // Replace with your OpenWeatherMap API key

/**
 * Fetch current weather based on city name.
 * @param {string} city - Name of the city.
 */
async function getCurrentWeather(city) {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`);
    if (!response.ok) throw new Error('Weather data not found');
    return await response.json();
}

/**
 * Fetch 5-day weather forecast based on city name.
 * @param {string} city - Name of the city.
 */
async function get5DayForecast(city) {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}`);
    if (!response.ok) throw new Error('Forecast data not found');
    return await response.json();
}

/**
 * Fetch weather based on geographical coordinates.
 * @param {number} lat - Latitude.
 * @param {number} lon - Longitude.
 */
async function getWeatherByCoordinates(lat, lon) {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`);
    if (!response.ok) throw new Error('Weather data not found');
    return await response.json();
}

/**
 * Fetch air quality data based on city name.
 * @param {string} city - Name of the city.
 */
async function getAirQuality(city) {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/air_pollution?q=${city}&appid=${apiKey}`);
    if (!response.ok) throw new Error('Air quality data not found');
    return await response.json();
}

/**
 * Fetch weather for multiple cities.
 * @param {Array<string>} cities - An array of city names.
 */
async function getMultipleCitiesWeather(cities) {
    return await Promise.all(cities.map(city => getCurrentWeather(city)));
}

// Example usage:
// getCurrentWeather('London').then(data => console.log(data));
// get5DayForecast('London').then(data => console.log(data));
// getWeatherByCoordinates(51.5074, -0.1278).then(data => console.log(data));
// getAirQuality('London').then(data => console.log(data));
// getMultipleCitiesWeather(['London', 'New York']).then(data => console.log(data));

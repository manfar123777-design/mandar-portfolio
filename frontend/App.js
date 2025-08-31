import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8001';

function App() {
  const [personalInfo, setPersonalInfo] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`${BACKEND_URL}/api/personal-info`);
        setPersonalInfo(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Loading Portfolio...</h1>
          <p className="text-gray-600">Connecting to backend...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center">
          <h1 className="text-6xl font-bold text-gray-900 mb-8">
            {personalInfo ? personalInfo.name : 'Mandar Farande'}
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Portfolio Website Coming Soon
          </p>
          <div className="bg-white p-8 rounded-lg shadow-lg max-w-md mx-auto">
            <h2 className="text-2xl font-semibold mb-4">Backend Status</h2>
            {personalInfo ? (
              <div className="text-green-600">
                ✅ Successfully connected to backend!
                <br />
                <small>Data loaded from database</small>
              </div>
            ) : (
              <div className="text-yellow-600">
                ⏳ Backend connected but no data yet
                <br />
                <small>Database might need setup</small>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

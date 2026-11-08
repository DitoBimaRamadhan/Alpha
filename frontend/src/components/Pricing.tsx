import React from 'react';

const Pricing = () => {
  const tiers = [
    { name: 'Free', price: '$0', features: ['5 Generations/mo', 'Basic AI Model'] },
    { name: 'Creator', price: '$19', features: ['100 Generations/mo', 'Better AI Model', 'Priority Support'] },
    { name: 'Pro', price: '$49', features: ['Unlimited Generations', 'Best AI Model', 'API Access'] },
  ];

  return (
    <div style={{ padding: '40px', textAlign: 'center' }}>
      <h2>Pricing Plans</h2>
      <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', marginTop: '20px' }}>
        {tiers.map((tier) => (
          <div key={tier.name} style={{ border: '1px solid #ddd', padding: '20px', borderRadius: '8px', width: '200px' }}>
            <h3>{tier.name}</h3>
            <p style={{ fontSize: '24px', fontWeight: 'bold' }}>{tier.price}/mo</p>
            <ul style={{ listStyle: 'none', padding: 0 }}>
              {tier.features.map((f) => <li key={f}>{f}</li>)}
            </ul>
            <button style={{ marginTop: '10px', padding: '10px', width: '100%' }}>Choose {tier.name}</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Pricing;

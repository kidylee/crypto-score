const request = require('supertest');
const { app, pool, server } = require('../app/app');
const { expect } = require('chai');

describe('GET /scores', () => {
  it('should return 400 if address or walletType are missing', async () => {
    const res = await request(app)
      .get('/scores')
      .expect(400);
    expect(res.text).equal('Bad Request: Address and walletType are required parameters');
  });

  it('should return 200 with pagination data and score data when address and walletType are provided', async () => {
    jest.spyOn(pool, 'getConnection').mockImplementation(() => {
      return {
        query: () => {
          return Promise.resolve([[],[]]);
        },
        release: () => {}
      }
    });
    const res = await request(app)
      .get('/scores?address=test&walletType=type&page=1&limit=10')
      .expect(200);
    expect(res.body).to.has.property("data");
    expect(res.body.page).to.equal("1");
    expect(res.body.limit).to.equal("10"); 
    pool.getConnection.mockRestore();
  });

  it('should return 500 if there is an error in the database query', async () => {
    jest.spyOn(pool, 'getConnection').mockImplementation(() => {
      throw new Error('Database connection error');
    });

    const res = await request(app)
      .get('/scores?address=test&walletType=type&page=1&limit=10')
      .expect(500);
    expect(res.text).equal('Internal Server Error');

    pool.getConnection.mockRestore();
  });

  afterAll(() => {
    pool.end();
    server.close(()=>{});
  });

});
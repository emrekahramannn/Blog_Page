TRENDS_DETAIL = """
<div class="container my-4">
    <!-- Make Columns Responsive -->
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
      <div class="col">
        <div class="card mb-3 shadow">
          <img src="../static/img/1.jpeg" alt="" class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">Lorem, ipsum.</h5>
            <p class="card-text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse,
              saepe!
            </p>
            <a href="/blogs/" class="btn btn-primary stretched-link">See Blogs</a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-3 shadow">
          <img src="../static/img/3.jpeg" alt="" class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">Lorem, ipsum.</h5>
            <p class="card-text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse,
              saepe!
            </p>
            <a href="/blogs/" class="btn btn-primary stretched-link">See Blogs</a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-3 shadow">
          <img src="../static/img/4.jpeg" alt="" class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">Lorem, ipsum.</h5>
            <p class="card-text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse,
              saepe!
            </p>
            <a href="/blogs/" class="btn btn-primary stretched-link">See Blogs</a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-3 shadow">
          <img src="../static/img/5.jpeg" alt="" class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">Lorem, ipsum.</h5>
            <p class="card-text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse,
              saepe!
            </p>
            <a href="/blogs/" class="btn btn-primary stretched-link">See Blogs</a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-3 shadow">
          <img src="../static/img/6.jpeg" alt="" class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">Lorem, ipsum.</h5>
            <p class="card-text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse,
              saepe!
            </p>
            <a href="/blogs/" class="btn btn-primary stretched-link">See Blogs</a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-3 shadow">
          <img src="../static/img/7.jpeg" alt="" class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">Lorem, ipsum.</h5>
            <p class="card-text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse,
              saepe!
            </p>
            <a href="/blogs/" class="btn btn-primary stretched-link">See Blogs</a>
          </div>
        </div>
      </div>
    </div>
  </div>
"""

CONTACT_DETAIL = """ 
<main>
      <div class="container my-5">
        <div class="row g-2">
          <div class="col-md-6 order-1 order-md-0">
            <iframe
              id="map"
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d195085.16496290543!2d28.836203049999988!3d40.182235399999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14ca05620c05be45%3A0xb41d1ba82a41bf94!2zTmlsw7xmZXIvQnVyc2E!5e0!3m2!1sen!2str!4v1719660931753!5m2!1sen!2str"
              width="100%"
              style="border: 0"
              allowfullscreen=""
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
            ></iframe>
          </div>
          <div class="col-md-6 order-0 order-md-1 mb-3 mb-md-0">
            <div class="card bg-dark">
              <div class="card-body">
                <div class="alert alert-warning">Please fill out the form</div>
                <form action="#" class="row g-3 text-white">
                  <div class="col-md-6">
                    <label for="email" class="form-label">Email</label>
                    <input
                      type="email"
                      name="email"
                      id="email"
                      class="form-control"
                    />
                  </div>
                  <div class="col-md-6">
                    <label for="name" class="form-label">Name</label>
                    <input
                      type="text"
                      name="name"
                      id="name"
                      class="form-control"
                    />
                  </div>
                  <div class="col-md-12">
                    <label for="phone" class="form-label">Phone</label>
                    <input
                      type="text"
                      name="phone"
                      id="phone"
                      class="form-control"
                    />
                  </div>
                  <div class="col-md-12">
                    <label for="subject" class="form-label">Subject</label>
                    <input
                      type="text"
                      name="subject"
                      id="subject"
                      class="form-control"
                    />
                  </div>
                  <div class="col-md-12">
                    <label for="message" class="form-label">Message</label>
                    <textarea name="message" id="message" class="form-control">
                    </textarea>
                  </div>
                  <div class="col-12">
                    <button class="btn btn-outline-warning" style="width: 100%">
                      Send Message
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
"""


FAKE_DB_PAGES = [
    {
        "url": "trends",
        "title": "Trends",
        "content": TRENDS_DETAIL,
    },
    {
        "url": "contact-us",
        "title": "Contact",
        "content": CONTACT_DETAIL,
    }
]
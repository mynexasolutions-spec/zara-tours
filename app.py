import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/events')
def events():
    return render_template('pages/events.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/gallery')
def gallery():
    # Get all images dynamically
    gallery_dir = os.path.join(app.static_folder, 'images', 'gallery')
    images = []
    
    if os.path.exists(gallery_dir):
        for root, dirs, files in os.walk(gallery_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    # Create a relative path for the template: 'images/gallery/folder/file.jpg'
                    rel_dir = os.path.relpath(root, app.static_folder)
                    images.append(os.path.join(rel_dir, file).replace('\\', '/'))
                    
    print(f"Gallery Dir: {gallery_dir}, Total Images: {len(images)}")
    return render_template('pages/gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

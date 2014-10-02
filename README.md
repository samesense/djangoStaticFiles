I'm trying to figure out why static file moment is broken on the FXI
site.  I was able to get the datepicker working here using STATIC_URL,
but not STATICFILES_DIRS. STATICFILES_DIRS broke moment. In the
template HTML, I have to add datepicker URLs w/o the static function
b/c the datepicker URLs are not found with the static utility. I'm
also putting the datepicker static files in the app directory: app/static/app/.

Go there to test: http://127.0.0.1:8000/dp/
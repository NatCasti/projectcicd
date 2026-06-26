def test_login(driver): 
    # AJUSTEMENT CLOUD 3 : Remplacement par une IP publique ou variable d'environnement 
    # Si APP_URL n'est pas fournie par GitHub, on utilise l'IP publique de votre Redmine 
    
    url = os.environ.get("APP_URL", "http://34.123.38.242") 
    username = os.environ.get("APP_USERNAME", "user1") 
    password = os.environ.get("APP_PASSWORD", "Hdjsy@1hrts") 
    driver.get(url + "/login") 
    driver.find_element(By.ID, "username").send_keys(username) 
    driver.find_element(By.ID, "password").send_keys(password) 
    driver.find_element(By.ID, "login-submit").click() 

    # Critère de succès 
    loggedas = driver.find_element(By.ID, "loggedas") 
    assert username in loggedas.text
def test_decimal_numbers(self, driver):
    """Test 6: Tester avec des nombres décimaux"""
    file_path = os.path.abspath("../src/index.html")
    driver.get(f"file://{file_path}")
    
    decimal_operations = [
        ("add", "3.5", "2.1", "5.6"),
        ("subtract", "10.7", "3.2", "7.5"),
        ("multiply", "2.5", "4.0", "10.0"),
        ("divide", "7.5", "2.5", "3.0")
    ]
    
    for op, num1, num2, expected in decimal_operations:
        driver.find_element(By.ID, "num1").clear()
        driver.find_element(By.ID, "num2").clear()
        
        driver.find_element(By.ID, "num1").send_keys(num1)
        driver.find_element(By.ID, "num2").send_keys(num2)
        
        select = Select(driver.find_element(By.ID, "operation"))
        select.select_by_value(op)
        
        driver.find_element(By.ID, "calculate").click()
        
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert f"Résultat: {expected}" in result.text
        time.sleep(0.5)

def test_negative_numbers(self, driver):
    """Test 7: Tester avec des nombres négatifs"""
    file_path = os.path.abspath("../src/index.html")
    driver.get(f"file://{file_path}")
    
    negative_operations = [
        ("add", "-5", "3", "-2"),
        ("subtract", "-10", "-5", "-5"),
        ("multiply", "-4", "3", "-12"),
        ("divide", "-8", "2", "-4")
    ]
    
    for op, num1, num2, expected in negative_operations:
        driver.find_element(By.ID, "num1").clear()
        driver.find_element(By.ID, "num2").clear()
        
        driver.find_element(By.ID, "num1").send_keys(num1)
        driver.find_element(By.ID, "num2").send_keys(num2)
        
        select = Select(driver.find_element(By.ID, "operation"))
        select.select_by_value(op)
        
        driver.find_element(By.ID, "calculate").click()
        
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert f"Résultat: {expected}" in result.text
        time.sleep(0.5)

def test_ui_elements(self, driver):
    """Test 8: Vérifier les propriétés CSS de l'interface"""
    file_path = os.path.abspath("../src/index.html")
    driver.get(f"file://{file_path}")
    
    # Tester les éléments d'entrée
    num1_input = driver.find_element(By.ID, "num1")
    num2_input = driver.find_element(By.ID, "num2")
    calculate_btn = driver.find_element(By.ID, "calculate")
    
    # Vérifier que les éléments sont visibles
    assert num1_input.is_displayed()
    assert num2_input.is_displayed()
    assert calculate_btn.is_displayed()
    
    # Vérifier les tailles
    assert num1_input.size['width'] > 0
    assert num1_input.size['height'] > 0
    
    # Vérifier les couleurs (optionnel, dépend de votre CSS)
    button_color = calculate_btn.value_of_css_property('background-color')
    assert button_color is not None
    
    # Vérifier la disponibilité du bouton
    assert calculate_btn.is_enabled()

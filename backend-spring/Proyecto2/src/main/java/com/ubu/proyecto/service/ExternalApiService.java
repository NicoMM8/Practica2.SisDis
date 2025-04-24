package com.ubu.proyecto.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class ExternalApiService {

    @Value("${api.python.url}")
    private String pythonApiUrl;

    public String callPythonApi() {
        RestTemplate restTemplate = new RestTemplate();
        // Realiza la llamada a la API en Python y retorna la respuesta
        return restTemplate.getForObject(pythonApiUrl, String.class);
    }
}

import type { EmailClassificationResult } from '@/@types/EmailClassificationResult'
import axios, { type AxiosInstance, isAxiosError } from 'axios'

class ApiService {
  private axiosInstance: AxiosInstance

  constructor() {
    this.axiosInstance = axios.create({
      baseURL: import.meta.env.VITE_API_BASE_URL,
      timeout: 15000,
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
  }

  /**
   * Envia os dados do e-mail para o endpoint de classificação.
   * @param formData Os dados do formulário contendo o texto ou o arquivo do e-mail.
   * @returns Promise que resolve com os dados da classificação.
   * @throws  ApiError em caso de falha na requisição.
   */
  public async classifyEmail(formData: FormData): Promise<EmailClassificationResult> {
    try {
      const response = await this.axiosInstance.post<EmailClassificationResult>(
        '/api/classify',
        formData,
      )

      return response.data
    } catch (error) {
      if (isAxiosError(error)) {
        const errorMessage =
          error.response?.data?.detail || 'Erro desconhecido ao processar a requisição.'
        console.error('Erro na API:', errorMessage)

        throw new Error(errorMessage)
      } else {
        console.error('Erro de rede ou inesperado:', error)
        throw new Error('Não foi possível conectar ao servidor. Verifique sua conexão.')
      }
    }
  }
}

export default new ApiService()

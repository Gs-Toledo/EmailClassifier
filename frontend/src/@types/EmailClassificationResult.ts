export interface EmailClassificationResult {
  filename: string
  classification: "Produtivo" | "Improdutivo"
  suggested_reply: string
}

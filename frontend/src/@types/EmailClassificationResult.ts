export interface EmailClassificationResult {
  filename: string | null
  classification: "Produtivo" | "Improdutivo" /* | string */
  suggested_reply: string
}
